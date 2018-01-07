import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import './Footer.css';
class Footer extends React.Component{
    constructor(props) {
        super(props)
    }
    componentWillMount() {
    }

    render(){
        return(
            <footer className="page-footer stylish-color-dark">
                <div className="container">
                    <div className="row text-center text-md-left mt-3 pb-3">
                        <div className="col-md-3 col-lg-3 col-xl-3 mx-auto mt-3">
                            <h6 className="title mb-4 font-bold">Light</h6>
                            <p>Here you can use rows and columns here to organize your footer content. Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
                        </div>
                        <hr className="w-100 clearfix d-md-none" />
                        <div className="col-md-2 col-lg-2 col-xl-2 mx-auto mt-3">
                            <h6 className="title mb-4 font-bold">Light</h6>
                            <p><a href="#!">Your Account</a></p>
                            <p><a href="#!">Suggestions</a></p>
                            <p><a href="#!">Join Project</a></p>
                            <p><a href="#!">Help</a></p>
                        </div>
                        <hr className="w-100 clearfix d-md-none" />
                        <div className="col-md-3 col-lg-2 col-xl-2 mx-auto mt-3">
                            <h6 className="title mb-4 font-bold">Candor</h6>
                            <p><a href="#!">About</a></p>
                            <p><a href="#!">Other Works</a></p>
                            <p><a href="#!">Website</a></p>
                            <p><a href="#!">Inquire</a></p>
                        </div>
                        <hr className="w-100 clearfix d-md-none" />
                        <div className="col-md-4 col-lg-3 col-xl-3 mx-auto mt-3">
                            <h6 className="title mb-4 font-bold">Contact</h6>
                            <p><i className="fa fa-home mr-3"></i> New York, NY 10012, US</p>
                            <p><i className="fa fa-envelope mr-3"></i> info@example.com</p>
                            <p><i className="fa fa-phone mr-3"></i> + 01 234 567 88</p>
                            <p><a className="btn-floating btn-sm rgba-white-slight mr-xl-4"><i className="fa fa-facebook"></i></a> <a className="btn-floating btn-sm rgba-white-slight mr-xl-4"><i className="fa fa-twitter"></i></a> <a className="btn-floating btn-sm rgba-white-slight mr-xl-4"><i className="fa fa-linkedin"></i></a></p>
                        </div>
                    </div>
                    <hr />
                    <div className="row py-3 d-flex align-items-center">
                        <div className="col-md-8 col-lg-9">
                            <p className="text-center text-md-left grey-text">© 2017 Copyright: <a href="https://www.MDBootstrap.com"><strong> MDBootstrap.com</strong></a></p>
                        </div>
                    </div>
                </div>
            </footer>
        )
    }
}
export default Footer;
