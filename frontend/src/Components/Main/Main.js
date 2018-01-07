import React, { Component } from 'react';
import Header from '../Header/Header';
import Card from '../Card/Card';
import Footer from '../Footer/Footer';

class Main extends React.Component{
    constructor(props) {
        super(props)
    }
    componentWillMount() {
    }

    render(){
        return(
            <div className="" id="home">
                <Header />
                <div className="container justify-content-center">
                    <Card />
                    <Card />
                    <Card />
                    <Card />
                    <Card />
                    <Card />
                </div>
                <Footer />
            </div>
        )
    }
}
export default Main;
