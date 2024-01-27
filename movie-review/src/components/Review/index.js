import './index.scss'

const Review = () => {


    return (
            // first grid contains card layout for looking at movie stats
            //second grid is where user leaves review: 

            //ToDo: 
            //  make grade two as a partial of grid one (expand onClick of leave a review)
            //  format elements in page to be responsive 

            <>      
                <h2 className="signup-h2"> Review Movie: </h2>
                <div className="row">
                    <div className="col-md-6 card-area">
                        <div className="card" style={{marginRight: 18 + 'em'}}>
                            <img src="https://images.unsplash.com/photo-1616530940355-351fabd9524b?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8bW92aWUlMjBwb3N0ZXJ8ZW58MHx8MHx8fDA%3D" class="card-img-top" alt="..."/>
                            <div className="card-body">
                                <h5 className="card-title">Movie Name</h5>
                                <p className="card-text">Brief sentence or two describing premise of movie</p>
                            </div>
                            <ul class="list-group list-group-flush">
                                <li className="list-group-item">likes</li>
                                <li className="list-group-item">reviews</li>
                                <li className="list-group-item">comments</li>
                            </ul>
                            <div class="card-body">
                                <a href="#" className="card-link">See all reviews</a>
                                <a href="#" className="card-link">Another link</a>
                                <a href="#" className="card-link btn btn-primary">Submit</a>
                            </div>
                        </div>
                </div>
                </div>
                <div className="row"> 
                    <div className="col-md-2 form-space-review"> 
                        <form>
                            <div className="form-group">
                                    <textarea></textarea>
                            </div>
                        </form> 
                        <buton className="btn btn-md btn-success submit-button" ><span className=" register-sp">Register</span></buton>
                    </div>
                </div>       
            </>
            
    );
}

export default Review