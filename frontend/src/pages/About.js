import React from "react";
import { Typography } from "@mui/material";
import Grid from "@mui/material/Grid";

const About = () => {
    return (
        <Grid
            item
            container
            direction="column"
            alignItems="center"
            justifyContent="flex-start"
            rowSpacing={5}
            wrap="nowrap"
            width="70%"
            paddingY="50px"
        >
            <Grid
                item
                container
                direction="column"
                alignItems="center"
                justifyContent="center"
                rowSpacing={3}
            >
                <Grid item>
                    <Typography variant="h2">
                        Airport Operation Management System
                    </Typography>
                </Grid>
                <Grid item>
                    <Typography variant="body1">
                        Beta International Airport (BIA), a private enterprise,
                        is a transparent organization dedicated to serving
                        our local community as well as the millions of travelers
                        who pass through our doors each year.
                        We welcome public interest in the way we do business.
                    </Typography>
                </Grid>
            </Grid>
            <Grid
                item
                container
                direction="column"
                alignItems="center"
                justifyContent="center"
                rowSpacing={3}
            >
                <Grid item>
                    <Typography variant="h2">The Developers</Typography>
                </Grid>
                <Grid item>
                    <Typography variant="body1">
                        CMPE 202 - Team Beta  |
                        Anesha  |
                        Varun  |
                        Shravani
                    </Typography>
                </Grid>
            </Grid>
        </Grid>
    );
};

export default About;
