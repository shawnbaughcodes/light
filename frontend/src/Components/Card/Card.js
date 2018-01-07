import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import './Card.css';
class Card extends React.Component{
    constructor(props) {
        super(props)
    }
    componentWillMount() {
    }

    render(){
        return(
            <div className="card">
                <h1 id="cardUser">User Name</h1>
                <div className="cardContent">
                    <p id="cardText">This will be some sort of review about some stuff.</p>
                    <img src="http://howlandechoes.com/wp-content/uploads/2016/04/MG_4821-Copyright-Dani-Hansen-730x410.jpg" className="rounded mx-auto d-block" id="cardImage" />
                </div>
                <div id="cardButtonsContainer">
                    <ul id="cardButtons">
                        <li><Link to="#">Helpful</Link></li>
                        <li><Link to="#">Comment</Link></li>
                        <li><Link to="#">Share</Link></li>
                    </ul>
                </div>
            </div>
        )
    }
}
export default Card;
