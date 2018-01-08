import axios from 'axios';

import {
    GET_ALL_REVIEWS
} from './types';

export const getAllReviews = () => async(dispatch) => {
    axios.get('/index')
        .then(response => {
            dispatch({ type: GET_ALL_REVIEWS, payload: response.data })
        })
}
