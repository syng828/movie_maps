
import './App.css';
import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';
import TitleInfo from './pages/TitlePage'; 
import ReviewPage from './pages/ReviewPage';
import React from 'react'; 
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { ApiProvider } from './context/ApiContext';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <ApiProvider>
          <Routes>
            <Route path = "/" element = {<Home/>}></Route>
            <Route path = "/login" element = {<Login/>}></Route>
            <Route path = "/register" element = {<Register/>}></Route>
            <Route path = "/title/:titleId" element = {<TitleInfo/>}></Route> 
            <Route path = "/review" element = {<ReviewPage/>}></Route> {/*Make dynamic later. */}
          </Routes>
        </ApiProvider>
      </BrowserRouter>
    </div>
  );
}

export default App;
