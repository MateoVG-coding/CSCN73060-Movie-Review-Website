import './index.scss'
import {Outlet} from 'react-router-dom'
import Navbar from '../Navbar/_Navbar'



const Layout = () => {

    //layout partial
    return(     
        <>      
            <Navbar/>
            <Outlet/>    
        </>
    );
}
export default Layout