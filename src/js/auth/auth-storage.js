const AUTH_KEY = "karbon_auth";

export function saveAuth(data) {
  localStorage.setItem(
    AUTH_KEY,

    JSON.stringify(data),
  );
}

export function getToken() {
  const auth = localStorage.getItem(AUTH_KEY);

  if (!auth) {
    return null;
  }

  return JSON.parse(auth).token;
}

export function logout() {
  localStorage.removeItem(AUTH_KEY);
}
