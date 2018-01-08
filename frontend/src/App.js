import React, { Component } from 'react';
import {BrowserRouter, Route} from 'react-router-dom'
import { Provider } from 'react-redux';
import ReduxThunk from 'redux-thunk';

import Store from './Store';
import './index.css';
import Main from './Components/Main/Main';
import Nav from './Components/Nav/Nav';
import Reviews from './Components/Reviews/Reviews';

class App extends Component {
    render() {
        return (
            <Provider store={Store}>
                <BrowserRouter>
                    <div className="App">
                        <Nav />
                        <Route exact path="/" component={Main} />
                        <Route path="/reviews" component={Reviews} />
                    </div>
                </BrowserRouter>
            </Provider>
        );
    }
}

export default App;
