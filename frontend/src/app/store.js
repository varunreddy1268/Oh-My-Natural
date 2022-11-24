import { configureStore } from '@reduxjs/toolkit';
import counterReducer from '../features/counter/counterSlice';
import userReducer from '../features/user/userSlice';
//import cartReducer from '../features/cart/cartSlice';


export const store = configureStore({
  reducer: {
    counter: counterReducer,
    user: userReducer,
  },
});
