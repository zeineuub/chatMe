import React, { useState } from "react";
import "./Register.css";
import { Link, useNavigate  } from "react-router-dom";

const Register = () => {
  const [formData, setFormData] = useState({
    firstname: "",
    lastname: "",
    email: "",
    password: "",
    confirmPassword: "",
  });
  const [errors, setErrors] = useState({});
  const navigate = useNavigate();
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevFormData) => ({
      ...prevFormData,
      [name]: value,
    }));
  };


  const validateForm = () => {
    const errors = {};

    if (formData.password.length < 8) {
      errors.passwordLength = "Le mot de passe doit contenir au moins 8 caractères";
    }

    if (!formData.password.match(/[A-Z]/)) {
      errors.passwordUppercase = "Le mot de passe doit contenir une lettre majuscule";
    }

    if (!formData.password.match(/\W/)) {
      errors.passwordSpecialCharacter = "Le mot de passe doit contenir un caractère spécial";
    }

    if (!formData.password.match(/\d/)) {
      errors.passwordNumber = "Le mot de passe doit contenir un chiffre";
    }

    if (formData.password !== formData.confirmPassword) {
      errors.passwordMatch = "Les mots de passe ne correspondent pas";
    }

    setErrors(errors);
    return Object.keys(errors).length === 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (validateForm()) {
        const payload={
            "firstname":formData.firstname,
            "lastname":formData.lastname,
            "email":formData.email,
            "password":formData.password
        }
        fetch(`${process.env.API_URL}/auth/register`, {
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify(payload)
        })
        .then((response)=>response.json())
        .then((data)=>{
            navigate("/sign-in"); // Redirect after successful registration
        })
        .catch((error) => {
          console.error("Error:", error);
          // Handle errors here if necessary
        });

    }
  };

  return (
    <div className="register-container">
      <p className="mx-auto text-center fs-5 text-gray-900">
        Ouvrez un compte en deux clics
      </p>
      <p className="mb-5 text-center fs-6 text-gray-500">
        Déjà inscrit ?{" "}
        <Link to="/login" className="custom-link">
          Se connecter
        </Link>
      </p>
      <form className="w-100" style={{ maxWidth: "400px" }} onSubmit={handleSubmit}>
        <div className="form-group mb-3">
          <input
            name="firstname"
            type="text"
            value={formData.firstname}
            onChange={handleChange}
            className="form-control"
            placeholder="Prénom"
          />
        </div>
        <div className="form-group mb-3">
          <input
            name="lastname"
            type="text"
            value={formData.lastname}
            onChange={handleChange}
            className="form-control"
            placeholder="Nom"
          />
        </div>
        <div className="form-group mb-3">
          <input
            name="email"
            type="email"
            value={formData.email}
            onChange={handleChange}
            className="form-control"
            placeholder="Email"
          />
        </div>
        <div className="form-group mb-3">
          <input
            name="password"
            type="password"
            value={formData.password}
            onChange={handleChange}
            className="form-control"
            placeholder="Mot de passe"
          />
        </div>
        <div className="form-group mb-3">
          <input
            name="confirmPassword"
            type="password"
            value={formData.confirmPassword}
            onChange={handleChange}
            className="form-control"
            placeholder="Confirmer le mot de passe"
          />
        </div>
        {errors.passwordLength && (
          <p className="mb-0 d-flex align-items-center">
            <i className="bi bi-x" style={{ color: "red", fontSize: "1.5rem" }}></i>
            {errors.passwordLength}
          </p>
        )}
        {errors.passwordUppercase && (
          <p className="mb-0 d-flex align-items-center">
            <i className="bi bi-x" style={{ color: "red", fontSize: "1.5rem" }}></i>
            {errors.passwordUppercase}
          </p>
        )}
        {errors.passwordSpecialCharacter && (
          <p className="mb-0 d-flex align-items-center">
            <i className="bi bi-x" style={{ color: "red", fontSize: "1.5rem" }}></i>
            {errors.passwordSpecialCharacter}
          </p>
        )}
        {errors.passwordNumber && (
          <p className="mb-0 d-flex align-items-center">
            <i className="bi bi-x" style={{ color: "red", fontSize: "1.5rem" }}></i>
            {errors.passwordNumber}
          </p>
        )}
        {errors.passwordMatch && (
          <p className="mb-0 d-flex align-items-center">
            <i className="bi bi-x" style={{ color: "red", fontSize: "1.5rem" }}></i>
            {errors.passwordMatch}
          </p>
        )}

        <button type="submit" className="btn text-light btn-block mb-3 w-100" style={{ backgroundColor: "#1D97D8" }}>
          S'inscrire
        </button>
      </form>
    </div>
  );
};


export default Register;