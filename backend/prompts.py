transcript_to_clip = 'Here is a transcript of a youtube video with time stamps in seconds. Decompose this video into many short videos.  Aim to keep the short videos below 3 minutes, but avoid unnatural splits that make the content more confusing to follow. Return a json of the clips that has a short title, description, the start point, and the end point. Ensure the end of one video is the start of the next:  '

example = "This is a 3. [4.22] It's sloppily written and rendered at an extremely low resolution of 28x28 pixels,  [6.06] but your brain has no trouble recognizing it as a 3. [10.769] And I want you to take a moment to appreciate how  [14.34] crazy it is that brains can do this so effortlessly. [16.604] I mean, this, this and this are also recognizable as 3s,  [19.7] even though the specific values of each pixel is very different from one  [23.019] image to the next. [27.271] The particular light-sensitive cells in your eye that are firing when  [28.9] you see this 3 are very different from the ones firing when you see this 3. [32.781] But something in that crazy-smart visual cortex of yours resolves these as representing  [37.52] the same idea, while at the same time recognizing other images as their own distinct  [42.8] ideas. [47.9] But if I told you, hey, sit down and write for me a program that takes in a grid of  [49.22] 28x28 pixels like this and outputs a single number between 0 and 10,  [54.699] telling you what it thinks the digit is, well the task goes from comically trivial to  [59.2] dauntingly difficult. [64.81] Unless you've been living under a rock, I think I hardly need to motivate the relevance  [67.16] and importance of machine learning and neural networks to the present and to the future. [70.9] But what I want to do here is show you what a neural network actually is,  [75.12] assuming no background, and to help visualize what it's doing,  [79.002] not as a buzzword but as a piece of math. [82.308] My hope is that you come away feeling like the structure itself is motivated,  [85.02] and to feel like you know what it means when you read,  [88.826] or you hear about a neural network quote-unquote learning. [91.509] This video is just going to be devoted to the structure component of that,  [95.36] and the following one is going to tackle learning. [98.3] What we're going to do is put together a neural  [100.96] network that can learn to recognize handwritten digits. [103.327] This is a somewhat classic example for introducing the topic,  [109.36] and I'm happy to stick with the status quo here,  [112.104] because at the end of the two videos I want to point you to a couple good  [114.272] resources where you can learn more, and where you can download the code that  [117.547] does this and play with it on your own computer. [120.955] There are many many variants of neural networks,  [125.04] and in recent years there's been sort of a boom in research towards these variants,  [127.715] but in these two introductory videos you and I are just going to look at the simplest  [132.301] plain vanilla form with no added frills. [136.996] This is kind of a necessary prerequisite for understanding any of the more powerful  [139.86] modern variants, and trust me it still has plenty of complexity for us to wrap our minds  [143.938] around. [148.26] But even in this simplest form it can learn to recognize handwritten digits,  [149.12] which is a pretty cool thing for a computer to be able to do. [153.248] And at the same time you'll see how it does fall  [157.48] short of a couple hopes that we might have for it. [159.855] As the name suggests neural networks are inspired by the brain, but let's break that down. [163.38] What are the neurons, and in what sense are they linked together? [168.52] Right now when I say neuron all I want you to think about is a thing that holds a number,  [172.5] specifically a number between 0 and 1. [178.082] It's really not more than that. [180.68] For example the network starts with a bunch of neurons corresponding to  [183.78] each of the 28x28 pixels of the input image, which is 784 neurons in total. [188.893] Each one of these holds a number that represents the grayscale value of the  [194.7] corresponding pixel, ranging from 0 for black pixels up to 1 for white pixels. [199.477] This number inside the neuron is called its activation,  [205.3] and the image you might have in mind here is that each neuron is lit up when its  [208.307] activation is a high number. [212.656] So all of these 784 neurons make up the first layer of our network. [216.72] Now jumping over to the last layer, this has 10 neurons,  [226.5] each representing one of the digits. [229.478] The activation in these neurons, again some number that's between 0 and 1,  [232.04] represents how much the system thinks that a given image corresponds with a given digit. [236.678] There's also a couple layers in between called the hidden layers,  [243.04] which for the time being should just be a giant question mark for  [246.473] how on earth this process of recognizing digits is going to be handled. [249.906] In this network I chose two hidden layers, each one with 16 neurons,  [254.26] and admittedly that's kind of an arbitrary choice. [257.912] To be honest I chose two layers based on how I want to motivate the structure  [261.019] in just a moment, and 16, well that was just a nice number to fit on the screen. [264.564] In practice there is a lot of room for experiment with a specific structure here. [268.78] The way the network operates, activations in one  [273.02] layer determine the activations of the next layer. [275.722] And of course the heart of the network as an information processing mechanism comes down  [279.2] to exactly how those activations from one layer bring about activations in the next layer. [283.863] It's meant to be loosely analogous to how in biological networks of neurons,  [289.14] some groups of neurons firing cause certain others to fire. [293.692] Now the network I'm showing here has already been trained to recognize digits,  [298.12] and let me show you what I mean by that. [301.625] It means if you feed in an image, lighting up all 784 neurons of the input layer  [303.64] according to the brightness of each pixel in the image,  [308.351] that pattern of activations causes some very specific pattern in the next layer  [311.609] which causes some pattern in the one after it,  [316.262] which finally gives some pattern in the output layer. [318.996] And the brightest neuron of that output layer is the network's choice,  [322.56] so to speak, for what digit this image represents. [326.573] And before jumping into the math for how one layer influences the next,  [332.56] or how training works, let's just talk about why it's even reasonable  [336.39] to expect a layered structure like this to behave intelligently. [340.114] What are we expecting here? [344.06] What is the best hope for what those middle layers might be doing? [345.4] Well, when you or I recognize digits, we piece together various components. [348.92] A 9 has a loop up top and a line on the right. [354.2] An 8 also has a loop up top, but it's paired with another loop down low. [357.38] A 4 basically breaks down into three specific lines, and things like that. [361.98] Now in a perfect world, we might hope that each neuron in the second  [367.6] to last layer corresponds with one of these subcomponents,  [371.615] that anytime you feed in an image with, say, a loop up top,  [375.049] like a 9 or an 8, there's some specific neuron whose activation is going to be close to 1. [378.541] And I don't mean this specific loop of pixels,  [384.5] the hope would be that any generally loopy pattern towards the top sets off this neuron. [386.957] That way, going from the third layer to the last one just requires  [392.44] learning which combination of subcomponents corresponds to which digits. [396.103] Of course, that just kicks the problem down the road,  [401.0] because how would you recognize these subcomponents,  [403.241] or even learn what the right subcomponents should be? [405.44] And I still haven't even talked about how one layer influences the next,  [408.06] but run with me on this one for a moment. [411.261] Recognizing a loop can also break down into subproblems. [413.68] One reasonable way to do this would be to first  [417.28] recognize the various little edges that make it up. [419.946] Similarly, a long line, like the kind you might see in the digits 1 or 4 or 7,  [423.78] is really just a long edge, or maybe you think of it as a certain pattern of several  [428.457] smaller edges. [433.491] So maybe our hope is that each neuron in the second layer of  [435.14] the network corresponds with the various relevant little edges. [438.868] Maybe when an image like this one comes in, it lights up all of the  [443.54] neurons associated with around 8 to 10 specific little edges,  [447.57] which in turn lights up the neurons associated with the upper loop  [451.244] and a long vertical line, and those light up the neuron associated with a 9. [455.215] Whether or not this is what our final network actually does is another question,  [460.68] one that I'll come back to once we see how to train the network,  [464.733] but this is a hope that we might have, a sort of goal with the layered structure  [467.986] like this. [472.039] Moreover, you can imagine how being able to detect edges and patterns  [473.16] like this would be really useful for other image recognition tasks. [476.808] And even beyond image recognition, there are all sorts of intelligent  [480.88] things you might want to do that break down into layers of abstraction. [484.057] Parsing speech, for example, involves taking raw audio and picking out distinct sounds,  [488.04] which combine to make certain syllables, which combine to form words,  [492.783] which combine to make up phrases and more abstract thoughts, etc. [496.556] But getting back to how any of this actually works,  [501.1] picture yourself right now designing how exactly the activations in one layer might  [503.735] determine the activations in the next. [507.993] The goal is to have some mechanism that could conceivably combine pixels into edges,  [510.86] or edges into patterns, or patterns into digits. [516.049] And to zoom in on one very specific example, let's say the  [519.44] hope is for one particular neuron in the second layer to pick  [523.024] up on whether or not the image has an edge in this region here. [526.792] The question at hand is what parameters should the network have? [531.44] What dials and knobs should you be able to tweak so that it's expressive  [535.64] enough to potentially capture this pattern, or any other pixel pattern,  [539.705] or the pattern that several edges can make a loop, and other such things? [543.714] Well, what we'll do is assign a weight to each one of the  [548.72] connections between our neuron and the neurons from the first layer. [551.868] These weights are just numbers. [556.32] Then take all of those activations from the first layer  [558.54] and compute their weighted sum according to these weights. [561.958] I find it helpful to think of these weights as being organized into a  [567.7] little grid of their own, and I'm going to use green pixels to indicate positive weights,  [571.146] and red pixels to indicate negative weights, where the brightness of  [575.576] that pixel is some loose depiction of the weight's value. [578.973] Now if we made the weights associated with almost all of the pixels zero  [582.78] except for some positive weights in this region that we care about,  [586.579] then taking the weighted sum of all the pixel values really just amounts  [590.117] to adding up the values of the pixel just in the region that we care about. [593.916] And if you really wanted to pick up on whether there's an edge here,  [599.14] what you might do is have some negative weights associated with the surrounding pixels. [602.439] Then the sum is largest when those middle pixels  [607.48] are bright but the surrounding pixels are darker. [610.09] When you compute a weighted sum like this, you might come out with any number,  [614.26] but for this network what we want is for activations to be some value between 0 and 1. [618.703] So a common thing to do is to pump this weighted sum into some function  [624.12] that squishes the real number line into the range between 0 and 1. [628.304] And a common function that does this is called the sigmoid function,  [632.46] also known as a logistic curve. [635.882] Basically very negative inputs end up close to 0,  [638.0] positive inputs end up close to 1, and it just steadily increases around the input 0. [641.185] So the activation of the neuron here is basically a  [649.12] measure of how positive the relevant weighted sum is. [652.705] But maybe it's not that you want the neuron to  [657.54] light up when the weighted sum is bigger than 0. [659.687] Maybe you only want it to be active when the sum is bigger than say 10. [662.28] That is, you want some bias for it to be inactive. [666.84] What we'll do then is just add in some other number like negative 10 to this  [671.38] weighted sum before plugging it through the sigmoid squishification function. [675.52] That additional number is called the bias. [680.58] So the weights tell you what pixel pattern this neuron in the second  [683.46] layer is picking up on, and the bias tells you how high the weighted  [687.366] sum needs to be before the neuron starts getting meaningfully active. [691.273] And that is just one neuron. [696.12] Every other neuron in this layer is going to be connected to  [698.28] all 784 pixel neurons from the first layer, and each one of  [702.546] those 784 connections has its own weight associated with it. [706.743] Also, each one has some bias, some other number that you add  [711.6] on to the weighted sum before squishing it with the sigmoid. [714.624] And that's a lot to think about! [718.11] With this hidden layer of 16 neurons, that's a total of 784 times 16 weights,  [719.96] along with 16 biases. [726.278] And all of that is just the connections from the first layer to the second. [728.84] The connections between the other layers also have  [732.52] a bunch of weights and biases associated with them. [734.93] All said and done, this network has almost exactly 13,000 total weights and biases. [738.34] 13,000 knobs and dials that can be tweaked and  [743.8] turned to make this network behave in different ways. [746.695] So when we talk about learning, what that's referring to is  [751.04] getting the computer to find a valid setting for all of these  [754.316] many many numbers so that it'll actually solve the problem at hand. [757.701] One thought experiment that is at once fun and kind of horrifying is to imagine sitting  [762.62] down and setting all of these weights and biases by hand,  [767.238] purposefully tweaking the numbers so that the second layer picks up on edges,  [770.282] the third layer picks up on patterns, etc. [774.375] I personally find this satisfying rather than just treating the network as a total  [776.98] black box, because when the network doesn't perform the way you anticipate,  [781.094] if you've built up a little bit of a relationship with what those weights and biases  [784.861] actually mean, you have a starting place for experimenting with how to change the  [789.074] structure to improve. [793.139] Or when the network does work but not for the reasons you might expect,  [794.96] digging into what the weights and biases are doing is a good way to challenge  [798.482] your assumptions and really expose the full space of possible solutions. [802.297] By the way, the actual function here is a little cumbersome to write down,  [806.84] don't you think? [810.004] So let me show you a more notationally compact way that these connections are represented. [812.5] This is how you'd see it if you choose to read up more about neural networks. 214 00:13:41,380 --> 00:13:40,520 Organize all of the activations from one layer into a column as a vector. [817.66] Then organize all of the weights as a matrix, where each row of that matrix corresponds  [821.38] to the connections between one layer and a particular neuron in the next layer. [830.137] What that means is that taking the weighted sum of the activations in  [838.54] the first layer according to these weights corresponds to one of the  [842.266] terms in the matrix vector product of everything we have on the left here. [845.94] By the way, so much of machine learning just comes down to having a  [854.0] good grasp of linear algebra, so for any of you who want a nice visual  [857.508] understanding for matrices and what matrix vector multiplication means,  [861.171] take a look at the series I did on linear algebra, especially chapter 3. [864.885] Back to our expression, instead of talking about adding the bias to each one of  [869.24] these values independently, we represent it by organizing all those biases into a vector,  [873.648] and adding the entire vector to the previous matrix vector product. [878.607] Then as a final step, I'll wrap a sigmoid around the outside here,  [883.28] and what that's supposed to represent is that you're going to apply the  [886.867] sigmoid function to each specific component of the resulting vector inside. [890.723] So once you write down this weight matrix and these vectors as their own symbols,  [895.94] you can communicate the full transition of activations from one layer to the next in an  [900.533] extremely tight and neat little expression, and this makes the relevant code both a lot  [905.463] simpler and a lot faster, since many libraries optimize the heck out of matrix  [910.393] multiplication. [914.819] Remember how earlier I said these neurons are simply things that hold numbers? [917.82] Well of course the specific numbers that they hold depends on the image you feed in,  [922.22] so it's actually more accurate to think of each neuron as a function,  [927.39] one that takes in the outputs of all the neurons in the previous layer and spits out a  [931.648] number between 0 and 1. [936.94] Really the entire network is just a function, one that takes in  [939.2] 784 numbers as an input and spits out 10 numbers as an output. [943.192] It's an absurdly complicated function, one that involves 13,000 parameters  [947.56] in the forms of these weights and biases that pick up on certain patterns,  [951.514] and which involves iterating many matrix vector products and the sigmoid  [955.469] squishification function, but it's just a function nonetheless. [959.318] And in a way it's kind of reassuring that it looks complicated. [963.4] I mean if it were any simpler, what hope would we have  [967.34] that it could take on the challenge of recognizing digits? [969.744] And how does it take on that challenge? [973.34] How does this network learn the appropriate weights and biases just by looking at data? [975.08] Well that's what I'll show in the next video, and I'll also dig a little  [980.14] more into what this particular network we're seeing is really doing. [983.236] Now is the point I suppose I should say subscribe to stay notified  [987.58] about when that video or any new videos come out,  [990.796] but realistically most of you don't actually receive notifications from YouTube, do you? [993.195] Maybe more honestly I should say subscribe so that the neural networks  [998.02] that underlie YouTube's recommendation algorithm are primed to believe  [1001.322] that you want to see content from this channel get recommended to you. [1004.624] Anyway, stay posted for more. [1008.56] Thank you very much to everyone supporting these videos on Patreon. [1010.76] I've been a little slow to progress in the probability series this summer,  [1014.0] but I'm jumping back into it after this project,  [1017.485] so patrons you can look out for updates there. [1019.762] To close things off here I have with me Lisha Li who did her PhD work on the  [1023.6] theoretical side of deep learning and who currently works at a venture capital  [1027.135] firm called Amplify Partners who kindly provided some of the funding for this video. [1030.762] So Lisha one thing I think we should quickly bring up is this sigmoid function. [1035.46] As I understand it early networks use this to squish the relevant weighted  [1039.7] sum into that interval between zero and one, you know kind of motivated  [1043.204] by this biological analogy of neurons either being inactive or active. [1046.569] Exactly. [1050.28] But relatively few modern networks actually use sigmoid anymore. [1050.56] Yeah. [1054.32] It's kind of old school right? [1054.44] Yeah or rather ReLU seems to be much easier to train. [1055.76] And ReLU, ReLU stands for rectified linear unit? [1059.4] Yes it's this kind of function where you're just taking a max of zero  [1062.68] and a where a is given by what you were explaining in the video and  [1067.469] what this was sort of motivated from I think was a partially by a  [1072.122] biological analogy with how neurons would either be activated or not. [1076.638] And so if it passes a certain threshold it would be the identity function but if it did  [1081.36] not then it would just not be activated so it'd be zero so it's kind of a simplification. [1086.073] Using sigmoids didn't help training or it was very difficult  [1091.16] to train at some point and people just tried ReLU and it happened  [1095.55] to work very well for these incredibly deep neural networks. [1100.301] All right thank you Lisha. [1105.1] "