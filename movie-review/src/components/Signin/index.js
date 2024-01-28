import './index.scss'

const SignIn = () => {
    return (
        <div className="row"> 
        <div className="col-md-3 col-sm-1 form-space"> 
            <h2 className="signin-h2"> Sign In </h2>
            <form>
                <div className="form-group">
                        <input type="text" className="form-control" id="username" placeholder='username' required/>
                </div>
                <div className="form-group">
                    <input type="password" className="form-control" id="passwordrepeat" placeholder='password' required/>
                </div>
            </form> 
            <buton className="btn btn-md btn-success submit-button" ><span className="login">Log In</span></buton>
        </div>
    </div>  
    );
}

export default SignIn