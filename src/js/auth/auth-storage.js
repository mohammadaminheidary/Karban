const AUTH_KEY = "karbon_auth";

export function saveAuth(data) {
  localStorage.setItem(
    AUTH_KEY,

    JSON.stringify(data),
  );
}

export function getAuth() {
  const data = localStorage.getItem(AUTH_KEY);

  return data ? JSON.parse(data) : null;
}

export function logout() {
  localStorage.removeItem(AUTH_KEY);
}
