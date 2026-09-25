const API_URL = "http://127.0.0.1:8000/api";


export async function loginUser(username, password) {
  const response = await fetch(`${API_URL}/login`, {
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


export async function validateToken(token) {
  const response = await fetch(`${API_URL}/auth/me`, {
    method: "GET",

    headers: {
      Authorization: `Bearer ${token}`,
    },
  });


  if (response.status === 401) {
    return null;
  }


  if (!response.ok) {
    throw new Error("Server error");
  }


  return await response.json();
}