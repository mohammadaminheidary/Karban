import { protectPage } from "../guards/auth-guard.js";

document.addEventListener("DOMContentLoaded", () => {
  protectPage();
});
