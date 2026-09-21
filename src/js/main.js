import { initLogin } from "./auth/login.js";
import { initPasswordToggle } from "./auth/login.js";

document.addEventListener("DOMContentLoaded", () => {
  initLogin();

  initPasswordToggle();
});
