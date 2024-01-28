

import './index.scss'











const SubmitReview = () => {
    return (
        <>
            <h1 className="submit-title">Write a Review</h1>
            <div className="row">
                <div className="col-md-6 offset-5 form-group">
                 <form className=" col-md-5 submit-review">
                    <div className="card" style={{marginRight: 18 + 'em'}}>
                        <img src="https://images.unsplash.com/photo-1616530940355-351fabd9524b?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8bW92aWUlMjBwb3N0ZXJ8ZW58MHx8MHx8fDA%3D" className="card-img-top" alt="..."/>
                        <div className="card-body">
                            <h5 className="card-title">Movie Name</h5>
                            <p className="card-text">
                                <span className="fas fa-thumbs-up"> 10k</span>
                                <span className="fas fa-star"> 3.5</span>
                            </p>
                        </div>
                        <div class="card-body">
                            <textarea type="text" className="form-control" id="email" required></textarea>
                        </div>               
                        <div class="card-body">
                            <a className="btn btn-success review-submit">Submit</a>
                        </div>               
                    </div>
                </form>
                </div>
            </div>
         
       </>

    );
}

export default SubmitReview


