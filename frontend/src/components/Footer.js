import React from 'react';
import { Grid, Typography } from "@mui/material";

const Footer = () => {
    return (
        <Grid
            item
            container
            alignItems="center"
            justifyContent="center"
            backgroundColor="primary.main"
            padding="40px"
        >
            <footer style={{ width: "100%" }}>
                <Grid
                    item
                    container
                    direction="row"
                    alignItems="center"
                    justifyContent="center"
                    rowSpacing={3}
                >
                    <Grid item xs={10} sm={5}>
                        <Typography variant="h3">
                            Airport  Management System - CMPE 202
                        </Typography>
                    </Grid>
                    <Grid item container direction="column" xs={10} sm={5} rowSpacing={1}>
                        <Grid item>
                            <Typography variant="h6">Developers</Typography>
                        </Grid>
                        <Grid item>
                            <Typography>Varun</Typography>
                        </Grid>
                        <Grid item>
                            <Typography>Anesha</Typography>
                        </Grid>
                        <Grid item>
                            <Typography>Shravani</Typography>
                        </Grid>
                    </Grid>
                </Grid>
            </footer>
        </Grid>
    );
};
export default Footer;
