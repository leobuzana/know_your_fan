import React, { useState, useEffect } from "react";
import { supabase } from "./supabaseClient";

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const user = supabase.auth.user();
    setUser(user);
  }, []);

  const signUp = async () => {
    const { user, error } = await supabase.auth.signUp({
      email: "email@example.com",
      password: "password123",
    });
    if (user) {
      setUser(user);
    }
    if (error) console.error("Error signing up:", error.message);
  };

  const signIn = async () => {
    const { user, error } = await supabase.auth.signIn({
      email: "email@example.com",
      password: "password123",
    });
    if (user) {
      setUser(user);
    }
    if (error) console.error("Error signing in:", error.message);
  };

  return (
    <div>
      <h1>Know Your Fan</h1>
      {!user ? (
        <div>
          <button onClick={signUp}>Sign Up</button>
          <button onClick={signIn}>Sign In</button>
        </div>
      ) : (
        <div>
          <h2>Welcome, {user.email}</h2>
          <button onClick={() => supabase.auth.signOut()}>Sign Out</button>
        </div>
      )}
    </div>
  );
}

export default App;
