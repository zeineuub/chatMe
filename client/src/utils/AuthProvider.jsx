import { createContext, useContext, useState } from "react";

// un context permet de partager des informations entre différents composants
// sans avoir à passer manuellement des props à chaque niveau de l'arborescence des composants. 
const AuthContext = createContext();
// AuthProvider est le composant principal qui wrap children et leur fournit les méthodes d'authentification
export const AuthProvider = ({ children }) => {
    const [token, setToken] = useState(null);  
    const login = (userToken) => {
        console.log(userToken)
        localStorage.setItem("access_token", userToken);
        setToken(userToken);
    }; 
    const logout = () => {
        setToken(null);
        localStorage.removeItem("access_token");
    };  
    const isAuthenticated = !!token;  // indique si l'utilisateur est authentifie
    return (
        <AuthContext.Provider value={{ isAuthenticated, login, logout }}>
        {children}
        </AuthContext.Provider>
    );
};
// useAuth c'est un hook qui permet d'utiliser les méthodes d'authentification
export const useAuth = () => {
    const context = useContext(AuthContext); // récupérer les valeurs de l'authContext (isAuthenticated, login, logout)
    if (!context) {
        throw new Error("useAuth must be used within an AuthProvider");
    }  return context;
};


// how to use it
/*
<AuthProvider>
    <App />
</AuthProvider>

*/
// inside any component
/*
const { isAuthenticated, login, logout } = useAuth();
if (isAuthenticated) {
  // do something
} else {
  // do something else
}
*/