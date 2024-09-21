import React from 'react';
import SignIn from '../Signin/SignIn';

import home from '../../assets/images/chatmebg.jpg';
import './Auth.css';
import { Outlet } from 'react-router-dom';
const Auth = () => {
    return (
        <div className="container-fluid vh-100 ">
            <div className="row h-100 d-flex">
                <div className="col-8 p-0 ">
                    <img src={home} alt="home" className="img-fluid vh-100" />
                </div>
                <div className="col-4 align-items-center justify-content-center ">
                <Outlet />
                </div>
            </div>
        </div>
    );
};

export default Auth;
