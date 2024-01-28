import './index.scss'
import {Outlet} from 'react-router-dom'
import Navbar from '../Navbar/_Navbar'



const Layout = () => {

    //layout partial
    return(     
        <>      
            <Navbar/>
            <div className="col-6 offset-3 half-background">
            </div>  
            <Outlet/> 
        </>
    );
}
export default Layout