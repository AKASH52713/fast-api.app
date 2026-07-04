// import Welcome from "./components/Welcome";
import NavBar from "./components/NavBar";
import Footer from "./components/Footer";
import CompanyCard from "./components/CompanyCard";
import JobCard from "./components/JobCard";
import Login from "./pages/login";
import Register from "./pages/Register";
import {useEffect, useState} from "react";
import { getCompanies } from "./Services/CompanyService";
import type { Company } from "./types/company";

type AuthView = "login" | "register" | "dashboard";

function App(){
  const[loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [companies, setCompanies] = useState<Company[]>([]);
  const [authView, setAuthView] = useState<AuthView>("login");
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) {
      setIsAuthenticated(true);
      setAuthView("dashboard");
    } else {
      setIsAuthenticated(false);
      setAuthView("login");
      setLoading(false);
    }
  }, []);

  async function fetchCompanies() {
    setLoading(true);
    try {
      const Companies = await getCompanies();
      setCompanies(Companies);
    } catch (error) {
      setError((error as Error).message);
    } finally{
      setLoading(false);
    }
  }

  useEffect(() => {
    if (isAuthenticated) {
      fetchCompanies();
    }
  }, [isAuthenticated]);

  const handleLogin = (token: string) => {
    localStorage.setItem("token", token);
    setIsAuthenticated(true);
    setAuthView("dashboard");
  };

  const handleLogout = () => {
    localStorage.removeItem("token");
    setIsAuthenticated(false);
    setAuthView("login");
  };

  const handleSwitchToRegister = () => {
    setAuthView("register");
  };

  const handleSwitchToLogin = () => {
    setAuthView("login");
  };

  if (authView === "login") {
    return <Login onLogin={handleLogin} onSwitchToRegister={handleSwitchToRegister} />;
  }

  if (authView === "register") {
    return <Register onRegister={handleLogin} onSwitchToLogin={handleSwitchToLogin} />;
  }

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div>
      <NavBar onLogout={handleLogout} />
      <br />
      <CompanyCard companies={companies} />
      <JobCard />
      <Footer />
    </div>
  )
}

export default App