import './index.scss'
import {useState, useEffect} from 'react'

const Signup = () => {

    //extract data from server fetch
    const [data, setData] = useState([{}])

    //fetch data from server
    useEffect (() => {
      const fetchRegisterData = async () => {
        try {
          const response = await fetch('/review');
          if(!response.ok) {
            throw new Error(`Network responded with: ${response.Error}`)
          }
          const data = await response.json();
          setData (data)
          console.log(data)
        } catch (error) {
          console.error ('Error fetching data: ', error);
        }
      };
  
      fetchRegisterData();
      // empty array present to prevent loop of get requests
      // TODO:
        //fix bug of two get requests issued when user clicks;
    }, [])

    return (
      <>
        <div className="row"> 
            <div className="col-md-3 col-sm-1 form-space"> 
                <h2 className="signup-h2"> Sign up today!</h2>
                <form>
                    <div className="form-group">
                            <input type="text" className="form-control" id="username" placeholder={data.username}/>
                    </div>
                    <div className="form-group">
                        <input type="password" className="form-control" id="passwordrepeat" placeholder={data.password}/>
                    </div>
                    <div className="form-group">
                        <input type="password" className="form-control" id="password" placeholder="Repeat Password"/>
                    </div>
                    <div className="form-group">
                        <input type="email" className="form-control" id="email" placeholder="name@example.com"></input>
                    </div>
                </form> 
                <buton className="btn btn-md btn-success submit-button" ><span className=" register-sp">Register</span></buton>
            </div>
        </div>       
       </>
    );
}

export default Signup