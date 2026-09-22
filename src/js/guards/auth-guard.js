import { getToken } from "../auth/auth-storage.js";

export function protectPage() {
  const token = getToken();

  if (!token) {
    window.location.href = "login-page.html";
  }
}
