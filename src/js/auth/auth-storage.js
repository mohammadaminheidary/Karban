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


  try {
    const parsedAuth = JSON.parse(auth);


    if (
      !parsedAuth ||
      typeof parsedAuth.token !== "string" ||
      !parsedAuth.token.trim()
    ) {
      localStorage.removeItem(AUTH_KEY);

      return null;
    }


    return parsedAuth.token;

  } catch (error) {
    localStorage.removeItem(AUTH_KEY);

    return null;
  }
}

export function logout() {
  localStorage.removeItem("karbon_auth");
}
