import React, { useState } from 'react';
import axios from 'axios';

function Signup() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const response = await axios.post('https://glowing-space-bassoon-6997vjxrp5r9259q7-3000.app.github.dev/', {
                email,
                password
            });
            console.log('Signup successful:', response.data);
            // Redirect or do something upon successful signup
        } catch (error) {
            console.error('Signup error:', error.response.data);
            // Handle errors (e.g., show error message)
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Email:
                <input type="email" value={email} onChange={e => setEmail(e.target.value)} required />
            </label>
            <label>
                Password:
                <input type="password" value={password} onChange={e => setPassword(e.target.value)} required />
            </label>
            <button type="submit">Sign Up</button>
        </form>
    );
}

export default Signup;
