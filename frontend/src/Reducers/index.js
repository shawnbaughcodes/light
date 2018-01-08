import { combineReducers } from 'redux';
import ReviewReducer from './ReviewReducer';

export default combineReducers({
    review: ReviewReducer
})
