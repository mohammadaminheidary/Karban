import { logout } from "../auth/auth-storage.js";
import { protectPage } from "../guards/auth-guard.js";


protectPage();


const logoutButton = document.getElementById(
  "logoutButton"
);


if (logoutButton) {
  logoutButton.addEventListener(
    "click",
    () => {
      logout();

      window.location.replace(
        "/page/login-page.html"
      );
    }
  );
}