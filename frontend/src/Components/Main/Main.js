import React, { Component } from 'react';
import { connect } from 'react-redux';

import * as actions from '../../Actions';

import Header from '../Header/Header';
import Card from '../Card/Card';
import Footer from '../Footer/Footer';

class Main extends React.Component{
    constructor(props) {
        super(props)
    }
    state = {
        reviews: []
    }
    componentWillMount() {
        this.props.getAllReviews()
    }
    componentWillReceiveProps = (nextProps) => {
        console.log(nextProps.review);
        this.setState({ reviews: nextProps.review })
        this.allReivews(nextProps)
    }
    allReivews = async(nextProps) => {
        await this.nextProps.review.map(
            review => <Card />
        )
    }
    render() {
        return(
            <div className="" id="home">
                <Header />
                <div className="container justify-content-center">
                    {this.componentWillReceiveProps}
                    <Card />
                    <Card />
                    <Card />
                </div>
                <Footer />
            </div>
        )
    }
}
function mapStateToProps({ review }) {
    return {
        review: review.reviews
    }
}
export default connect(mapStateToProps, actions)(Main);
