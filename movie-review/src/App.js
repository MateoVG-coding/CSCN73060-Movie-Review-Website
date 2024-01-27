import './App.scss';
import React from 'react'
import {Routes, Route} from 'react-router-dom'
import Layout from './components/Layout'
import Home from './components/Home'
import Signup from './components/Signup'
import Review from './components/Review'



const App = () => {

  return(
    //routes to be rendered
      <>
      <Routes>
        <Route path="/" element={<Layout/>}>
          <Route index element={<Home/>}/>
          <Route path="signup" element={<Signup/>}/>
          <Route path ="review" element={<Review/>}/>
        </Route>      
      </Routes>     
      </>     
  ); 
}


export default App;
