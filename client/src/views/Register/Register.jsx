import React, { useState } from "react";
import "./Register.css";
import { Link } from "react-router-dom";

const Register = () => {
    const [email,setEmail] = useState("");
    const [password,setPassword] = useState("");
    const [confirmePassword,setConfirmePassword] = useState("");
    const  [firstname,setFirstname] = useState("");
    const [lastname,setLastname] = useState("");
    return (
        <div className="register-container">            
                
                <p className="mx-auto text-center fs-5 text-gray-900">Ouvrez un compte en deux clics </p>
                <p className="mb-5 text-center fs-6 text-gray-500">Déjà inscrit ? <Link to="/sign-in" className="custom-link ">Se connecter</Link></p>
            <form className="w-100 " style={{ maxWidth: "400px" }}>
                <div className="form-group mb-3">
                    <input name="firstname" type="text" className="form-control" placeholder="Prénom" />
                </div>
                <div className="form-group mb-3">
                    <input name="lastname" type="text" className="form-control" placeholder="Nom" />
                </div>
                <div className="form-group mb-3">
                    <input name="email" type="email" className="form-control" placeholder="Email" />
                </div>
                <div className="form-group mb-3">
                    <input name="password" type="password" className="form-control" placeholder="Mot de passe" />
                </div>
                <div className="form-group mb-3">
                    <input name="confirm_password" type="password" className="form-control" placeholder=" Confirmer le mot de passe" />
                </div>
                <p name="caracter-length" className="d-flex align-items-center mb-0">
                    <i className="bi bi-x" style={{ color: "red", fontSize: "1.5rem" }}></i>
                    Le mot de passe comporte plus de 8 caractères
                </p>
                <p name="special-caracter" className="d-flex align-items-center mb-0">
                    <i className="bi bi-x" style={{ color: "red", fontSize: "1.5rem"}}></i>
                    Le mot de passe comporte un caractère spécial
                </p>
                <p name="caracter-number" className="d-flex align-items-center mb-0">
                    <i className="bi bi-x" style={{ color: "red", fontSize: "1.5rem" }}></i>
                    Le mot de passe comporte un chiffre
                </p>
                <p name="caracter-uppercase" className="d-flex align-items-center mb-0">
                    <i className="bi bi-x" style={{ color: "red", fontSize: "1.5rem"}}></i>
                    Le mot de passe comporte une lettre majuscule
                </p>
                <p name="matching-password" className="d-flex align-items-center mb-0">
                    <i className="bi bi-x" style={{ color: "red", fontSize: "1.5rem"}}></i>
                    Les mots de passe correspondent
                </p>
                <button type="submit" className="btn text-light btn-block mb-3 w-100" style={{ backgroundColor: "#1D97D8"}}>Inscrivez-vous</button>
            </form>
        </div>
    );
};

export default Register;