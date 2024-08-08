
import './App.css'
import Home from './views/Home/Home'
import { BrowserRouter, Routes, Route,Navigate  } from "react-router-dom";
import SignIn from './views/Signin/SignIn';
import Register from './views/Register/Register';
function App() {

  return (
    <BrowserRouter>
      <Routes>
      <Route path='/' element={<Home />} >
        <Route index element={<Navigate to="sign-in" replace />} />
          <Route path="sign-in" element={<SignIn />} />
          <Route path="register" element={<Register />} />
      </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App
