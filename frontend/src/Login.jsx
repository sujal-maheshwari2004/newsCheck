import { useState } from "react";

export default function Login() {

  const API_URL = import.meta.env.VITE_API_URL;

  const [email, setEmail] = useState("");
  const [loading, setLoading] = useState(false);

  async function sendLoginLink() {

    if (!email) return;

    setLoading(true);

    try {

      const res = await fetch(`${API_URL}/auth/request-login`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email: email
        })
      });

      const data = await res.json();

      if (!res.ok) {
        throw new Error(data.detail || "Failed to send login link.");
      }

      alert("Login link sent. Please check your email.");

    } catch (err) {

      console.log(err);
      alert(err.message);

    }

    setLoading(false);
  }

  return (
    <div className='min-h-[95vh] flex flex-col items-center justify-center'>

      <h1 className='text-foreground text-3xl font-semibold text-center'>
        Login
      </h1>

      <p className='text-muted-foreground text-md text-center m-4 w-[90%] md:max-w-[80%] lg:max-w-[50%]'>
          Enter your email to log in. My API key costs real money and I’d like to keep at least <em>some</em> of it.
      </p>

      <input
        className='bg-background border-border border rounded-md text-foreground placeholder-muted-foreground p-3 mt-7 mb-7 w-[90%] md:max-w-[70%] lg:max-w-[40%]'
        placeholder='you@example.com'
        value={email}
        onChange={e => setEmail(e.target.value)}
      />

      <button
        className={`${loading ? 'bg-muted-foreground border-muted-foreground' : 'bg-foreground border-foreground'} text-background border rounded-md py-[10px] w-36 font-semibold ${loading ? '' : 'hover:bg-background hover:text-foreground'} transition duration-300`}
        onClick={sendLoginLink}
        disabled={loading}
      >
        {loading ? "Sending..." : "Login"}
      </button>

    </div>
  );

}
