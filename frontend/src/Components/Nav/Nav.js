import React, { Component } from 'react';
import { Link } from 'react-router-dom';

import './Nav.css';

class Nav extends React.Component{
    constructor(props) {
        super(props)
    }
    componentWillMount() {
    }

    render(){
        return(
            <nav className="navbar navbar-toggleable-md navbar sticky-top navbar-light bg-faded">
                <button className="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <Link className="navbar-brand" to="#">Light</Link>
                <div className="collapse navbar-collapse justify-content-center" id="navbarNavAltMarkup">
                    <div className="navbar-nav">
                        <Link className="nav-item nav-link" to="/">Home</Link>
                        <Link className="nav-item nav-link" to="#">Reviews</Link>
                        <Link className="nav-item nav-link" to="/news">News</Link>
                        <Link className="nav-item nav-link" to="#">Account</Link>
                    </div>
                </div>
            </nav>
        )
    }
}
export default Nav;
