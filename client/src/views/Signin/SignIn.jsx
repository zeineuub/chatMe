import React, { useState } from 'react';
import icon from '../../assets/images/iconchatme.png';
import './SignIn.css';
import { Link } from "react-router-dom";

const SignIn = () => {
    const [state , setState] = useState({
        email : "",
        password : "",

    })
    const handleChange = (e) => {
        const {id , value} = e.target   
        setState(prevState => ({
            ...prevState,
            [id] : value
        }))
    }
    function handleSubmit(e) {
        const payload={
            "email":state.email,
            "password":state.password,
        }
    }

    return (
        <div className="signin-container">            
            <div className="text-center mb-4">
                <img src={icon} alt="chatme" className="img-fluid mb-3" style={{ width: '100px' }} />
                <p>👋 Marhabé</p>
            </div>
            <form className="w-100 " style={{ maxWidth: '400px' }}>
                <div className="form-group mb-3">
                    <input name="email" type="email" onChange={handleChange} value={email} className="form-control" placeholder="Email" />
                </div>
                <div className="form-group mb-3">
                    <input name="password" type="password"onChange={handleChange}  value={password} className="form-control" placeholder="Mot de passe" />
                </div>
                <button type="submit" className="btn text-light btn-block mb-3 w-100" onClick={handleSubmit} style={{ backgroundColor: '#1D97D8'}}>Se connecter</button>
                <div className="text-center mb-3">
                    <a href="./forget-password" className="text-decoration-none">Mot de passe oublié ?</a>
                </div>
                <div className="text-center">
                    <p>Pas encore inscrit ?<Link to="/register" className="text-decoration-none">Inscrivez-vous</Link></p>
                </div>
            </form>
        </div>
    );
};

export default SignIn;