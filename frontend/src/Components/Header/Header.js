import React, { Component } from 'react';
import { Link } from 'react-router-dom';

class Nav extends React.Component{
    constructor(props) {
        super(props)
    }
    componentWillMount() {
    }

    render(){
        return(
            <div className="jumbotron jumbotron-fluid">
                <div className="container">
                    <h1 className="display-3">Light</h1>
                    <p className="lead">Light is an app that you can do stuff on. Like writing reviews about bars and venues and concerts. You can also see the latest news in entertainment.</p>
                </div>
            </div>
        )
    }
}
export default Nav;
