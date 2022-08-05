# Online 3D Bin Packing with Constrained Deep Reinforcement Learning

![teaser](pictures/state_architecture.png)

## News!
> Hey guys:
>
> Thank you very much for your attention to this repo and active discussions on online BPP issues. To be honest, I didn't expect the repo to get attention when I released it and I'm clumsy with project maintenance. The good news is that an updated version of online 3D BPP solver is now being published, and this work has been accepted by [ICLR 2022](https://iclr.cc/Conferences/2022). 
>
> The link to my new work:  
> 
> [Paper: Learning Efficient Online 3D Bin Packing on Packing Configuration Trees](https://openreview.net/forum?id=bfuGjlCwAq) 
> 
> [New Code: Online-3D-BPP-PCT](https://github.com/alexfrom0815/Online-3D-BPP-PCT)
>
> Compared to the previous work, the advantages of this repo are:
>- [x] Container (bin) and item sizes can be set arbitrarily.
>- [x] Continuous online 3D-BPP is allowed and the environment is provided.
>- [x] Algorithms to approximate stability are provided ([see our other work](https://arxiv.org/abs/2108.13680v2))). 
>- [x] Better performance and the ability to account for more complex constraints.
>- [x] More adequate heuristic baselines for domain development.
>- [x] More stable training.
>- [x] No need to manually register gym anymore.
>
> If you are interested in online 3D BPP, I strongly recommend you to take a look. If you think it useful, **please star it**! Thank you very much!


## Introduction
```
This repository contains the implementation of paper [Online 3D Bin Packing with Constrained Deep Reinforcement Learning](https://arxiv.org/pdf/2006.14978.pdf).

Any contribution is welcome! If you have any recurring problems, please contact me at alexfrom0815@gmail.com.
```

## Install

```
To make this project work, there are two things you should do:
* Install python packages in 'requirements.py' (by 'pip install -r requirements.txt').
* Register our binpacking environment(envs/Bpp-v0) in your gym (discussed in https://github.com/openai/gym/issues/626).
* (This code works on Python 3.7)
```

## Run
We provide an unified interface in 'main.py'. There are examples of running our project.

For training：
```
Example: Train a new model on sequences generated randomly.
You can run 'python main.py --mode train --load-model False --use-cuda --item-seq sample'.
It will take about one day to get a model with satisfying performance.

You can run 'python main.py --help' for some information of common parameters.
There are many other parameters of our project in 'config.py', all of them are given default values.You can change it if you like.
```

For test:
```
Example:
If you want to test a model trained on sequences generated by CUT-2 Algorithm(get more details in our article).
You can run 'python main.py --mode test --load-model True --use-cuda --data-name cut_2.pt --load-name default_cut_2.pt'.

If you want see how the model work in lookahead setting,
You can run 'python main.py --mode test --load-model True --use-cuda --data-name cut_2.pt --load-name default_cut_2.pt --preview x', x is the lookahead number.

Codes of user-study application, multi-bin algorithm, MCTS for comparison are also provided,
Please check 'user_study/', 'multi_bin/', 'MCTS/' for details.
```

## Tips
```
* Different input state sizes need different kinds of CNN for encoding, you can adjust the network architecture in ./acktr/model.py to satisfy your needs. 

* Predicted mask is mainly for reducing MCTS computing costs. If you only need BPP-1 model, you can replace predicted mask with ground-truth mask during the training and it will be easy for training.

* If you relax the constraint of stability rules, you may get a better result, but it may be dangerous in practice.

* The computing overhead of our implementation is sensitive to the length of network layer, you should aviod a large network layer appears in your network architecture. 

* Bin packing problem's difficulty is related to its item set. The trained model's performance is also affected by it.
```

## Statement
```
Hang Zhao and Qijin She are co-authors of this repository.

Some codes are modified from opensource project 'pytorch-a2c-ppo-acktr-gail' (https://github.com/ikostrikov/pytorch-a2c-ppo-acktr-gail).
```

## License
```
Note that this source code is released only for academic use. Please do not use it for commercial purpose without authorization of the authors. The method is being patent protected. For commercial use, please contact Kai Xu (kevin.kai.xu@gmail.com).
```

## Citation

If you are interested, please cite the following paper:

```shell
@inproceedings{DBLP:conf/aaai/ZhaoS0Y021,
  author    = {Hang Zhao and
               Qijin She and
               Chenyang Zhu and
               Yin Yang and
               Kai Xu},
  title     = {Online 3D Bin Packing with Constrained Deep Reinforcement Learning},
  booktitle = {Thirty-Fifth {AAAI} Conference on Artificial Intelligence, {AAAI}
               2021, Thirty-Third Conference on Innovative Applications of Artificial
               Intelligence, {IAAI} 2021, The Eleventh Symposium on Educational Advances
               in Artificial Intelligence, {EAAI} 2021, Virtual Event, February 2-9,
               2021},
  pages     = {741--749},
  publisher = {{AAAI} Press},
  year      = {2021},
  url       = {https://ojs.aaai.org/index.php/AAAI/article/view/16155},
  timestamp = {Wed, 02 Jun 2021 18:09:11 +0200},
  biburl    = {https://dblp.org/rec/conf/aaai/ZhaoS0Y021.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```