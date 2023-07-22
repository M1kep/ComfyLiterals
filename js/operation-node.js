import {app} from "/scripts/app.js";

app.registerExtension({
    name: "ComfyLiterals.OperationNode",
    nodeCreated(node, app) {
        if (node['comfyClass'] === 'Operation') {
            const onAdded = node.onAdded
            node.onAdded = function (graph) {
                console.log("OperationNode onAdded")
                const firstCallbackResp = onAdded ? onAdded.apply(this, arguments) : undefined;

                /**
                 * @type {Record<string, INodeInputSlot>}
                 */
                const inputCache = {
                    "A": node.inputs[1],
                    "B": node.inputs[3]
                }

                if (this.widgets_values) {
                    const aType = this.widgets_values[0]
                    const bType = this.widgets_values[1]

                    // [IntA, FloatA, IntB, FloatB]
                    const aIdxToDelete = aType === "INT" ? 1 : 0
                    // [*A, IntB, FloatB]
                    const bIdxToDelete = bType === "INT" ? 3 : 1

                    inputCache["A"] = node.inputs[aIdxToDelete]
                    this.removeInput(aIdxToDelete)
                    inputCache["B"] = node.inputs[bIdxToDelete]
                    this.removeInput(bIdxToDelete)
                } else {
                    // Nodes being restored/pasted don't have widget_values
                    // Node has 4 inputs(IntA, FloatA, IntB, FloatB)
                    // Remove both float inputs, Float B moves to index 2 after Float A is removed
                    this.removeInput(1)
                    this.removeInput(2)
                }

                // Add a toggle widget to the node
                this.widgets[0].callback = function (v, canvas, node) {
                    addInputAtIndex(node, inputCache["A"], 0)
                    inputCache["A"] = node.inputs[1]
                    node.removeInput(1)
                }
                this.widgets[1].callback = function (v, canvas, node) {
                    addInputAtIndex(node, inputCache["B"], 2)
                    inputCache["B"] = node.inputs[1]
                    node.removeInput(1)
                }
            }
        }
    }
})

/**
 * Adds an input to a node at the given index.
 * @param node {LGraphNode}
 * @param input {INodeInputSlot}
 * @param index {number}
 * @returns {INodeInputSlot}
 */
function addInputAtIndex(node, input, index) {
    if (!node.inputs) {
        node.inputs = [];
    }

    if (index > node.inputs.length) {
        console.warn("LiteGraph: Warning adding port index: " + index + " of node " + node.id + ", it doesnt have so many inputs");
        node.inputs.push(input);
    } else {
        node.inputs.splice(index, 0, input);
    }
    if (node.onInputAdded) {
        node.onInputAdded(input);
    }
    node.setSize(node.computeSize());
    LiteGraph.registerNodeAndSlotType(node, input.type || 0);

    node.setDirtyCanvas(true, true);
    return input;
}
