import React, { Component } from 'react';
import {BrowserRouter, Route} from 'react-router-dom'
import './index.css';
import Main from './Components/Main/Main';
import Nav from './Components/Nav/Nav';

class App extends Component {
  render() {
    return (
        <BrowserRouter>
            <div className="App">
                <Nav />
                <Route exact path="/" component={Main} />
            </div>
        </BrowserRouter>
    );
  }
}

export default App;
