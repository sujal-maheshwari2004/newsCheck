import { useEffect } from "react";
import { useSearchParams } from "react-router-dom";

export default function Verify() {

  const API_URL = import.meta.env.VITE_API_URL;

  const [params] = useSearchParams();

  useEffect(() => {

    async function verifyLogin() {

      const token = params.get("token");

      if (!token) {
        alert("Invalid login link.");
        window.location.href = "/";
        return;
      }

      try {

        const res = await fetch(`${API_URL}/auth/verify?token=${token}`);

        const data = await res.json();

        if (!res.ok) {
          throw new Error(data.detail || "Login failed.");
        }

        localStorage.setItem("auth_token", data.token);

        window.location.href = "/";

      } catch (err) {

        console.log(err);
        alert(err.message);
        window.location.href = "/login";

      }

    }

    verifyLogin();

  }, []);

  return (
    <div className='min-h-[95vh] flex flex-col items-center justify-center'>

      <h1 className='text-foreground text-3xl font-semibold text-center'>
        Logging you in...
      </h1>

      <p className='text-muted-foreground text-md text-center m-4'>
        Please wait while we verify your login link.
      </p>

    </div>
  );

}
