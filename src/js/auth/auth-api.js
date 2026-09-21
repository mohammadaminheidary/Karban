const API_URL = "http://127.0.0.1:8000/api/login";

export async function loginUser(username, password) {
  const response = await fetch(API_URL, {
    method: "POST",

    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify({
      username,

      password,
    }),
  });

  if (!response.ok) {
    throw new Error("Server error");
  }

  return await response.json();
}
