import "./index.scss" 

const Home = () => {

    //home page:

    //TODO:
    // add carousel of top reveiwed movies 
    //carousel to match card formatting seend in leave review page

    return (
        <>
            <h1 className="movies">Movies</h1>
            <div className="row">
                    <div className="col-md-6 movie-card">
                        <div className="card" style={{marginRight: 18 + 'em'}}>
                            <img src="https://images.unsplash.com/photo-1616530940355-351fabd9524b?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8bW92aWUlMjBwb3N0ZXJ8ZW58MHx8MHx8fDA%3D" class="card-img-top" alt="..."/>
                            <div className="card-body">
                                <h5 className="card-title">Movie Name</h5>
                                <p className="card-text">
                                    <span className="fas fa-thumbs-up"> 10k</span>
                                    <span className="fas fa-star"> 3.5</span>
                                </p>
                            </div>
                            <div class="card-body">
                                <a href="/submitreview" className="card-link btn btn-primary">Add Review</a>
                                <a href="#" className="card-link fas fa-heart"></a>
                            </div>
                        </div>
                    </div>

                    <div className="col-md-6 offset-2 movie-card">
                        <div className="card" style={{marginRight: 18 + 'em'}}>
                            <img src="https://images.unsplash.com/photo-1616530940355-351fabd9524b?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8bW92aWUlMjBwb3N0ZXJ8ZW58MHx8MHx8fDA%3D" class="card-img-top" alt="..."/>
                            <div className="card-body">
                                <h5 className="card-title">Movie Name</h5>
                                <p className="card-text">
                                    <span className="fas fa-thumbs-up"> 10k</span>
                                    <span className="fas fa-star"> 3.5</span>
                                </p>
                            </div>
                            <div class="card-body">
                                <a href="submitreview" className="card-link btn btn-primary">Add Review</a>
                                <a href="#" className="card-link fas fa-heart"></a>
                            </div>
                        </div>
                    </div>

                    <div className="col-md-6 offset-4 movie-card">
                        <div className="card" style={{marginRight: 18 + 'em'}}>
                            <img src="https://images.unsplash.com/photo-1616530940355-351fabd9524b?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8bW92aWUlMjBwb3N0ZXJ8ZW58MHx8MHx8fDA%3D" class="card-img-top" alt="..."/>
                            <div className="card-body">
                                <h5 className="card-title">Movie Name</h5>
                                <p className="card-text">
                                    <span className="fas fa-thumbs-up"> 10k</span>
                                    <span className="fas fa-star"> 3.5</span>
                                </p>
                            </div>
                            <div class="card-body">
                                <a href="#submitreview" className="card-link btn btn-primary">Add Review</a>
                                <a href="#" className="card-link fas fa-heart"></a>
                            </div>
                        </div>
                    </div>
                </div>

                   <div className="row second-row">
                    <div className="col-md-6 movie-card2">
                        <div className="card" style={{marginRight: 18 + 'em'}}>
                            <img src="https://images.unsplash.com/photo-1616530940355-351fabd9524b?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8bW92aWUlMjBwb3N0ZXJ8ZW58MHx8MHx8fDA%3D" class="card-img-top" alt="..."/>
                            <div className="card-body">
                                <h5 className="card-title">Movie Name</h5>
                                <p className="card-text">
                                    <span className="fas fa-thumbs-up"> 10k</span>
                                    <span className="fas fa-star"> 3.5</span>
                                </p>
                            </div>
                            <div class="card-body">
                                <a href="/submitreview" className="card-link btn btn-primary">Add Review</a>
                                <a href="#" className="card-link fas fa-heart"></a>
                            </div>
                        </div>
                    </div>

                    <div className="col-md-6 offset-2 movie-card2">
                        <div className="card" style={{marginRight: 18 + 'em'}}>
                            <img src="https://images.unsplash.com/photo-1616530940355-351fabd9524b?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8bW92aWUlMjBwb3N0ZXJ8ZW58MHx8MHx8fDA%3D" class="card-img-top" alt="..."/>
                            <div className="card-body">
                                <h5 className="card-title">Movie Name</h5>
                                <p className="card-text">
                                    <span className="fas fa-thumbs-up"> 10k </span>
                                    <span className="fas fa-star"> 3.5 </span>
                                </p>
                            </div>
                            <div class="card-body">
                                <a href="/submitreview" className="card-link btn btn-primary">Add Review</a>
                                <a href="#" className="card-link fas fa-heart"></a>
                            </div>
                        </div>
                    </div>

                    <div className="col-md-6 offset-4 movie-card2">
                        <div className="card" style={{marginRight: 18 + 'em'}}>
                            <img src="https://images.unsplash.com/photo-1616530940355-351fabd9524b?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8bW92aWUlMjBwb3N0ZXJ8ZW58MHx8MHx8fDA%3D" class="card-img-top" alt="..."/>
                            <div className="card-body">
                                <h5 className="card-title">Movie Name</h5>
                                <p className="card-text">
                                    <span className="fas fa-thumbs-up"> 10k</span>
                                    <span className="fas fa-star"> 3.5</span>
                                </p>
                            </div>
                            <div class="card-body">
                                <a href="/submitreview" className="card-link btn btn-primary">Add Review</a>
                                <a href="#" className="card-link fas fa-heart"></a>
                            </div>
                        </div>
                    </div>
                </div>     
        </>

    );
}

export default Home