import React from 'react'
import {FormControl, FormControlLabel, FormGroup, FormHelperText, FormLabel, Switch} from "@mui/material";


export default function Gate() {
    const [state, setState] = React.useState({
        gate1: true,
        gate2: false,
        gate3: true,
    });

    const handleChange = (event) => {
        setState({
            ...state,
            [event.target.name]: event.target.checked,
        });
    };

    return (
        <FormControl component="fieldset" variant="standard">
            <FormLabel component="legend">Gate Management</FormLabel>
            <FormGroup>
                <FormControlLabel
                    control={
                        <Switch checked={state.gate1} onChange={handleChange} name="gate1" />
                    }
                    label="Gate 1"
                />
                <FormControlLabel
                    control={
                        <Switch checked={state.gate2} onChange={handleChange} name="gate2" />
                    }
                    label="Gate 2"
                />
                <FormControlLabel
                    control={
                        <Switch checked={state.gate3} onChange={handleChange} name="gate3" />
                    }
                    label="Gate 3"
                />
            </FormGroup>
            <FormHelperText>Helper text</FormHelperText>
        </FormControl>
    );
}

