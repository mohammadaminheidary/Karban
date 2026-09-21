export function validateLogin(username, password) {
  if (!username) {
    return {
      success: false,

      message: "نام کاربری را وارد کنید",
    };
  }

  if (!password) {
    return {
      success: false,

      message: "رمز عبور را وارد کنید",
    };
  }

  return {
    success: true,
  };
}
