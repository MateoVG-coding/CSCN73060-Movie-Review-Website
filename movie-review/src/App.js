import './App.scss';
import React from 'react'
import {Routes, Route} from 'react-router-dom'
import Layout from './components/Layout'
import Home from './components/Home'
import Signup from './components/Signup'
import SignIn from './components/Signin';
import Review from './components/Review'
import SubmitReview from './components/SubmitReview';



const App = () => {

  return(
    //routes to be rendered
      <>
      <Routes>
        <Route path="/" element={<Layout/>}>
          <Route index element={<Home/>}/>
          <Route path="signup" element={<Signup/>}/>
          <Route path="signin" element={<SignIn/>}/>
          <Route path ="review" element={<Review/>}/>
          <Route path ="submitreview" element={<SubmitReview/>}/>
        </Route>      
      </Routes>     
      </>     
  ); 
}


export default App;
