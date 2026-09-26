from collections import defaultdict, deque
from time import monotonic


MAX_ATTEMPTS = 5
WINDOW_SECONDS = 60


_failed_attempts = defaultdict(deque)


def _remove_expired_attempts(
    client_key: str,
    now: float,
):

    attempts = _failed_attempts[
        client_key
    ]

    while (
        attempts
        and now - attempts[0]
        >= WINDOW_SECONDS
    ):
        attempts.popleft()


def check_login_rate_limit(
    client_key: str,
):

    now = monotonic()

    _remove_expired_attempts(
        client_key,
        now,
    )

    attempts = _failed_attempts[
        client_key
    ]

    if len(attempts) < MAX_ATTEMPTS:
        return False, 0

    retry_after = int(
        WINDOW_SECONDS
        - (now - attempts[0])
    )

    return True, max(
        retry_after,
        1,
    )


def record_login_failure(
    client_key: str,
):

    now = monotonic()

    _remove_expired_attempts(
        client_key,
        now,
    )

    _failed_attempts[
        client_key
    ].append(now)


def clear_login_failures(
    client_key: str,
):

    _failed_attempts.pop(
        client_key,
        None,
    )