import { validateToken } from "../auth/auth-api.js";
import { getToken } from "../auth/auth-storage.js";


function redirectToLogin() {
  window.location.replace(
    "/page/login-page.html"
  );
}


export async function protectPage() {
  const token = getToken();


  if (!token) {
    redirectToLogin();

    return false;
  }


  try {
    const auth = await validateToken(token);


    if (!auth?.success) {
      localStorage.removeItem(
        "karbon_auth"
      );

      redirectToLogin();

      return false;
    }


    return true;

  } catch (error) {
    console.error(
      "Authentication validation failed:",
      error
    );


    redirectToLogin();

    return false;
  }
}