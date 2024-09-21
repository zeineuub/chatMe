import React, { useState } from 'react';
import icon from '../../assets/images/iconchatme.png';
import './SignIn.css';
import { Link, useNavigate } from "react-router-dom";
import 'react-toastify/dist/ReactToastify.css';
import { ToastContainer, toast } from 'react-toastify';
import { useAuth } from '../../utils/AuthProvider';

const SignIn = () => {
    const [state, setState] = useState({
        email: "",
        password: "",
    });

    const { login } = useAuth();
    const navigate = useNavigate();

    const handleChange = (e) => {
        const { name, value } = e.target;
        setState(prevState => ({
            ...prevState,
            [name]: value
        }));
    }

    const validateEmail = () => {
        if (!state.email) {
            toast.error("Email is required", {
                position: toast.POSITION.TOP_RIGHT,
            });
            return false;
        } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(state.email)) {
            toast.error("Invalid email format", {
                position: toast.POSITION.TOP_RIGHT,
            });
            return false;
        } else {
            return true;
        }
    };

    const validatePassword = () => {
        if (!state.password) {
            toast.error("Password is required", {
                position: toast.POSITION.TOP_RIGHT,
            });
            return false;
        } else {
            return true;
        }
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        if (!validateEmail() || !validatePassword()) {
            return;
        }

        const payload = {
            email: state.email,
            password: state.password,
        };

        fetch(`${process.env.API_URL}/auth/login`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Invalid credentials');
                }
                return response.json();
            })
            .then(data => {
                const { access_token, user } = data;
                console.log(access_token);
                login(access_token);
                localStorage.setItem("user", JSON.stringify(user));
                navigate("/home");
            })
            .catch(error => {
                toast.error("Échec de la connexion : Identifiants incorrects");
            });
    }

    return (
        <div className="signin-container">
            <div className="text-center mb-4">
                <img src={icon} alt="chatme" className="img-fluid mb-3" style={{ width: '100px' }} />
                <p>👋 Marhabé</p>
            </div>
            <form className="w-100" style={{ maxWidth: '400px' }} onSubmit={handleSubmit}>
                <div className="form-group mb-3">
                    <input name="email" type="email" onChange={handleChange} onBlur={validateEmail} value={state.email} className="form-control" placeholder="Email" />
                </div>
                <div className="form-group mb-3">
                    <input name="password" type="password" onChange={handleChange} onBlur={validatePassword} value={state.password} className="form-control" placeholder="Mot de passe" />
                </div>
                <button type="submit" className="btn text-light btn-block mb-3 w-100" style={{ backgroundColor: '#1D97D8' }}>Se connecter</button>
                <div className="text-center mb-3">
                    <Link to="/forget-password" className="text-decoration-none">Mot de passe oublié ?</Link>
                </div>
                <div className="text-center">
                    <p>Pas encore inscrit ? <Link to="/register" className="text-decoration-none">Inscrivez-vous</Link></p>
                </div>
            </form>
            <ToastContainer />
        </div>
    );
};

export default SignIn;
