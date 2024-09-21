
import './App.css'
import Auth from './views/Auth/Auth'
import { BrowserRouter, Routes, Route,Navigate  } from "react-router-dom";
import SignIn from './views/Signin/SignIn';
import Register from './views/Register/Register';
import Home from './views/Home/Home';
import { AuthProvider } from './utils/AuthProvider';
import  PrivateRoutes from './utils/PrivateRoutes';
function App() {

  return (
    <BrowserRouter>
    <AuthProvider>
        {" "}
      <Routes>
      <Route path='/' element={<Auth />} >
        <Route index element={<Navigate to="/login" replace />} />
          <Route path="/login" element={<SignIn />} />
          <Route path="register" element={<Register />} />
      </Route>
      <Route element={<PrivateRoutes />}>
        <Route path='/home' element={<Home />} ></Route>
      </Route>
      </Routes>
    </AuthProvider>
    </BrowserRouter>
  )
}

export default App
