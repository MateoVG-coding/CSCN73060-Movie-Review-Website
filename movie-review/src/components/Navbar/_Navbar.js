import'./Navbar.scss'

const Navbar = () => {

    return (
        //navbar partial
        //TO DO:
            //map all links to  correct routes
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand" href="/">Movies</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
            <li class="nav-item active">
                <a class="nav-link" href="/">All Movies</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="/signup">Create Account</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#">Sign-In</a>
            </li>
            <li class="nav-item">
            <a class="nav-link" href="/Review">Reviewed Movies</a>
            </li>
            </ul>
        </div>
        </nav>

    );
 
}

export default Navbar
    