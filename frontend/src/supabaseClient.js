import { createClient } from "@supabase/supabase-js";

export const supabase = createClient(
  "https://your-project-id.supabase.co", // URL do seu Supabase
  "your-anon-key" // Chave pública
);
