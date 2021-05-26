# Coding Challenge

## Overview

First of all, we really appreciate the time you have already spent with us, and look forward to seeing your work on this challenge!

This challenge was created with the intent that you can use it to showcase some of your more lower-level software engineering skills that you might not have been able to showcase throughout your journey with us so far.

With that in mind, we are more interested in seeing how you think and go about solving problems than we are with judging your code as we would a full time professional developer. Please feel free to use [Pseudocode](https://en.wikipedia.org/wiki/Pseudocode) or submit even unfinished code that has enough comments to show your intent.

## The Problem

We have some raw data about our customers in JSON format that we would like to gain some insights on. Our Product Manager would like to know how the breakdown of `Members per State` from the given data, so that she can effectively target where to spend her development dollars.

## Data format

We have managed to extract data from our legacy database and transform it into a simple [JSON](https://en.wikipedia.org/wiki/JSON) file that looks like this:

```json
[
  {
    "address": "3 Kennedy Elbow\nHancockfurt, SA, 2898",
    "firstName": "Shannon",
    "active": false,
    "lastName": "Robertson",
    "id": 0
  },
  {
    "firstName": "Christopher",
    "address": "Unit 57\n 3 Rachel Broadway\nKimberlytown, SA, 2674",
    "lastName": "Becker",
    "active": true,
    "id": 1
  },
  {
    "lastName": "Acevedo",
    "active": true,
    "id": 2,
    "firstName": "Steven",
    "address": "Suite 036\n 7 Tyler Avenue\nBrownland, QLD, 2627"
  }
]
```

### Data generation

[Faker](https://faker.readthedocs.io/en/master/) was used to generate the sample data, you can see the python code under `/scripts/generator/py`. I am not a python developer, but it is a great generator. I guess it can be good for some things.

You can run it yourself if you have python installed - I didn't get around to dockerising it so you're on your own with your dependencies and all that.

You can run it via:

```bash
$ python generator.py
```

## The output

Since the product team have asked for this data, the output must be able to work in their existing toolset - Excel. A simple [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) file output will be sufficient.

Below is a representation as to what is expected from the input seen above. Order does not matter, neither to states with a zero count (however, you may include them if you wish).

```csv
SA, 2
QLD, 1
```

## The ask

### Choose a language

We will accept your work in any language you choose. We realise that this is a graduate position so we will not be as strict as you might think.

**Partly working code is more than acceptable** - we even give you the opportunity to provide us with a solution written entirely in [Pseudocode](https://en.wikipedia.org/wiki/Pseudocode), remember we are more interested in seeing how you think to solve problems than seeing the most elegant code out there :)

### Use Git

Fork this repo into your own [GitHub](https://github.com/) account, if you do not already have one we recommend you sign up as it is a great resource to find resources that will help you on your journey regardless!

Once you have forked the repo, start writing your code in the `solution` directory found there.

You will find a `members-sample.json` file under the `/data` directory for you to play with. There is also a zip file containing a dataset of ~15000 members for you to test your code on.

## Hints and tips

### Commenting

Since we are using this exercise to see how you problem solve, please comment as much as you like. Over comment! Comment more than you usually would to show us your thinking.

We have placed a README.md file (similar to this one) in the `/solution` directory filled with thoughts, instructions, and how to run your code.

Here is a [Markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) in case you have never used it before.

### Testing / Automation

Although we generally look long and hard at testing practices when we look at engineers, this is not a requirement for you. If you would like to test your code as you go then that is great, however you will not be affected either way.

### Keep it simple

KISS is one of the oldest and most effective principles of software engineering. Keep it simple and try not to overcomplicate things.

### Reach out

Below you have the email address of Dean Baker, he will be as responsive as possible and will probably federate out to other members of his team. Don't be surprised if you get someone else replying to your query :)

## Contact us

If you have any questions about the coding challenge, any at all, please email Dean Baker directly - dean.baker@pexa.com.au
